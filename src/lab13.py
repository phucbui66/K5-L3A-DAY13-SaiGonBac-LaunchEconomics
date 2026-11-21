"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1 or (k is not None and (not isinstance(k, int) or k < 1)):
        raise ValueError('Cần 0 < p <= 1 và k là số nguyên dương')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    so_lan_chay_ky_vong(p, k)  # kiểm tra đầu vào
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=token.sum(), tool=tool.sum(),
                chay_lai=(token + tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(token.sum() + tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print('\nA3: theo loại yêu cầu (chi phí simulated)')
    for loai, nhom in reqs.groupby('loai'):
        kq = mo_hinh(runs, nhom)
        print(f"{loai:10s} n={len(nhom):4d} thành công={kq['thanh_cong']/len(nhom):.2%} lần/yc={nhom.so_lan_chay.mean():.2f} cps={kq['cps']:,.0f}")
    print('\nB1: độ nhạy (chi phí simulated)')
    kich_ban = {'Token x2': dict(gia_vao=52, gia_ra=260), 'Token x0.5': dict(gia_vao=13, gia_ra=65),
                'Xem lại x2': dict(he_so_xem_lai=2), 'Xem lại x0.5': dict(he_so_xem_lai=.5),
                'Làm lại x2': dict(he_so_lam_lai=2), 'Làm lại x0.5': dict(he_so_lam_lai=.5),
                'Lương +25%': dict(luong_phut=2500), 'Tối đa 2 lần': dict(max_lan_chay=2),
                'Tối đa 1 lần': dict(max_lan_chay=1),
                'Token và xem lại x2': dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2)}
    for ten, kw in kich_ban.items():
        kq = mo_hinh(runs, reqs, **kw)
        print(f"{ten:24s} {kq['cps']:,.0f} đ  {(kq['cps']/ket_qua['cps']-1)*100:+.1f}%")
    print('\nB3: chi phí cả hệ thống (simulated)')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        print(f"{k} lần: trợ lý={kq['tong']:,.0f}; không thành công={khong_thanh_cong}; cả hệ thống={kq['tong']+khong_thanh_cong*BASELINE:,.0f}; cps={kq['cps']:,.0f}")
    print('\nA4 và B4: phạm vi nội địa và hàng nặng (simulated)')
    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    scoped = mo_hinh(runs, scope)
    ok_ids = runs[(runs.status == 'ok') & runs.request_id.isin(scope.request_id)].request_id.nunique()
    rework = (scope.ket_qua == 'lam_lai').sum()
    print(f"Trong phạm vi: {len(scope)} yêu cầu, {scoped['thanh_cong']} thành công, {ok_ids} có lần chạy ok, {rework} làm lại")
    for volume in (45000, 22500):
        fixed = 40000000 / (volume * scoped['thanh_cong'] / len(reqs))
        print(f"{volume:,} yêu cầu/tháng: cố định/việc={fixed:,.0f}; cps gồm cố định={scoped['cps']+fixed:,.0f}")
    for minutes in (9, 15.3):
        cost = (scoped['token'] + scoped['tool'] + ok_ids * 5 * LUONG_PHUT + rework * minutes * LUONG_PHUT) / scoped['thanh_cong']
        print(f'Xem lại 100%, làm lại {minutes} phút: {cost:,.0f} đ/việc')
    print('\nD1: cỡ mẫu (công thức so hai tỷ lệ trong đề)')
    from statistics import NormalDist
    def co_mau(p1, p2):
        za, zb = NormalDist().inv_cdf(.975), NormalDist().inv_cdf(.8)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)
    for mde in (.05, .06):
        print(f'MDE {mde:.0%}: {co_mau(.70, .70 + mde)} yêu cầu mỗi nhóm')
    print(f"Theo nhân viên m=75: DE=2.48, cần {math.ceil(co_mau(.70,.75)*2.48)} yêu cầu và {math.ceil(co_mau(.70,.75)*2.48/75)} nhân viên mỗi nhóm; 20 cụm/nhóm có giới hạn hiệu dụng < 1000")
