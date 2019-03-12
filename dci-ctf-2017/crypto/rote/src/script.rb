out = File.read('rote.png').bytes.map { |x|
  ((x + 3) & 255).chr
}.join

File.write("../dist/rote.png", out)
