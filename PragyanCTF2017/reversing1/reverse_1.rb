class Fixnum
  def random_split(set = nil, repeats = false)
    p self
    set ||= 1..self
    p set
    set = [*set]
    print "After "
    p set
    return if set.empty? || set.min > self || set.inject(0, :+) < self
    tried_numbers = []
    while (not_tried = (set - tried_numbers).select {|n| n <= self }).any?
      tried_numbers << number = not_tried.sample
      return [number] if number == self
      new_set = set.dup
      new_set.delete_at(new_set.index(number)) unless repeats
      randomized_rest = (self-number).random_split(new_set, repeats)
      return [number] + randomized_rest if randomized_rest
    end
  end
end

class String
  def ^( other )
    b1 = self.unpack("U*")
    b2 = other.unpack("U*")
    longest = [b1.length,b2.length].max
    b1 = [0]*(longest-b1.length) + b1
    b2 = [0]*(longest-b2.length) + b2
    b1.zip(b2).map{ |a,b| a^b }.pack("U*")
  end
end

a2= Array.new
a= Array.new
string = gets
a=string.upcase.chars
sum = 0
length1 = a.length

for i in 0..a.length-1  ## /n is worth 10 characters change to length-1 at the end
  a[i] = (a[i].ord)^61
  sum = sum + a[i].ord
end
print "After uppercase and xor"
p a
for i in 0..length1-1
  a2[i] = a[i].to_i.random_split(20..30)
end
# Print the final output array which will be used for reversing
for i in 0..a2.length-1
  print a2[i].join(" ") + " "
end
