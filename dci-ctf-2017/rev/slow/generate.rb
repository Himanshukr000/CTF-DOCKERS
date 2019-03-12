flag = "DCI{t4ste_th3_4vr}"

flag.bytes.each.with_index do |b, i|
  puts "int v#{i} = #{(b << 3) ^ ((i + 1) * 3)};"
end


puts

puts "void send_flag() {"

flag.bytes.each.with_index do |b, i|
  puts "  Serial.print((char)((v#{i} ^ #{(i + 1) * 3}) >> 3));"
  puts "  for(int i = 0; i < 3600; i++) {"
  puts "    for(int j = 0; j < 24; j++) {"
  puts "       delay(1000);"
  puts "    }"
  puts "  }"
end

puts "  Serial.println();"

puts "}"
