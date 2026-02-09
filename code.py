def tallestBillboard(rods):
    dp = {0: 0}
    for rod in rods:
        new_dp = dict(dp)
        for d, s in dp.items():
            # Adding to left
            new_d = d + rod
            new_s = s + rod
            if new_d in new_dp:
                if new_s > new_dp[new_d]:
                    new_dp[new_d] = new_s
            else:
                new_dp[new_d] = new_s
            # Adding to right
            new_d = d - rod
            new_s = s + rod
            if new_d in new_dp:
  