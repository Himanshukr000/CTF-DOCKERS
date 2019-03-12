words = "- .... . / ..-. .-.. .- --. / .. ... / -- --- .-. ... . .. ... -. --- - -.. . .- -.. -.-- . -".split('/').map(&:strip)

puts words.inspect

space = 7
char = 3
tick = 0.2

def ping
  # puts [Time.new.to_f, "ping"]
  puts `ping -c 1 192.168.0.3`
end

words.each do |word|

  word.chars.each do |char|
    if char == ' '
      sleep tick * 3
    else
      ping

      if char == '.'
        sleep tick
      elsif char == '-'
        sleep tick * 3
      end
    end
  end

  sleep tick * 7
end
