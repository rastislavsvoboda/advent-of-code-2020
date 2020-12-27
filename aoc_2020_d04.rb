groups = File.open('4.in').read.split("\n\n")

passports = groups.map { |g| g.split.map { |x| x.split ?: }.to_h }

def year(s, e)
    ->x{ x =~ /^\d\d\d\d$/ && (s..e) === x.to_i } 
end

reqs = { 
    'byr' => year(1920, 2002),
    'iyr' => year(2010, 2020),
    'eyr' => year(2020, 2030),
    'hgt' => ->x{ x =~ /^\d+cm$/ && (150..193) === x.to_i || x =~ /^\d+in$/ && (59..76) === x.to_i },
    'hcl' => /^#[\da-f]{6}$/.method(:match?),
    'ecl' => /^amb|blu|brn|gry|grn|hzl|oth$/.method(:match?),
    'pid' => /^\d{9}$/.method(:match?)    
}

def is_valid1?(passport, reqs)
    reqs.keys.all? { |k| passport.key? k }
end

res1 = passports.count { |x| is_valid1?(x,reqs) } 
puts res1 # 219

def is_valid2?(passport, reqs)
    reqs.all? { |k,v| passport[k] && v.(passport[k]) }
end

res2 = passports.count { |x| is_valid2?(x,reqs) } 
puts res2 # 127
