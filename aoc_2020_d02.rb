input = File.readlines('2.in')

def is_valid1?(i1,i2,c,s)
    cnt = s.count(c)
    return i1 <= cnt && cnt <= i2
end

def is_valid2?(i1,i2,c,s)
    return (s[i1-1] == c) != (s[i2-1] == c)
end

entries = input.map { |line| i1,i2,c,s = line.scan /\w+/; [i1.to_i, i2.to_i, c, s] }
res1 = entries.count { |i1,i2,c,s| is_valid1?(i1,i2,c,s) }
res2 = entries.count { |i1,i2,c,s| is_valid2?(i1,i2,c,s) }
puts res1,res2
