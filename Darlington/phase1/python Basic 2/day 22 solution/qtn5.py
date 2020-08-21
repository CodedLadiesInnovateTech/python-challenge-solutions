# program to test AB and CD are orthogonal or not.
while True:
    try:
        print("Input xp, yp, xq, yq, xr, yr, xs, ys:")
        x_p, y_p, x_q, y_q, x_r, y_r, x_s, y_s = map(float, input().split())
        pq_x, pq_y = x_q - x_p, y_q - y_p
        rs_x, rs_y = x_s - x_r, y_s - y_r
        rs = pq_x*rs_x + pq_y*rs_y
        if abs(rs) > 1e-10:
            print("AB and CD are not orthogonal!")
        else:
            print("AB and CD are orthogonal!")
    except:
        break