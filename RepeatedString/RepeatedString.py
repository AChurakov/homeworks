def get_most_com_sub(s):
        sub = {}
        max_value = 0
        for i in range(len(s)):
            count = 0
            sub_value  = s[i]
            while i+1 < len(s) and s[i] <= s[i+1]:
                count += 1
                i += 1
                sub_value += s[i]
            sub[count] = sub.get(count, sub_value)
            max_value = max(sub.keys())
        return s.count(sub[max_value])


print(get_most_com_sub(input()))
