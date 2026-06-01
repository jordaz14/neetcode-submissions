class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            n_times, sub_str = k, [s[i]]
            for j in range(i+1, len(s)):
                if sub_str[-1] == s[j]:
                    sub_str.append(s[j])
                    ans = max(ans, len(sub_str))
                elif n_times > 0:
                    freq_c = max(sub_str, key=sub_str.count)
                    sub_str.append(freq_c)
                    n_times -= 1
                    ans = max(ans, len(sub_str))
                else:
                    ans = max(ans, len(sub_str))
                    break

        return ans