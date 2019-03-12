# coding: utf-8

def reg_no(reg)
  reg.to_s[1].to_i - 1
end

class Program
  def initialize
    @insts = []
    @symbols = {}
  end

  def label(name)
    @symbols[name] = ip
  end

  def ip
    @insts.size
  end

  def set(reg, value)
    x = 1
    x <<= 4
    x |= reg_no(reg)

    @insts << x

    @insts << (value & 0xff)
    @insts << (value >> 8)
  end

  def mov(reg1, reg2)
    x = 2 << 4
    x |= reg_no(reg1)
    x |= reg_no(reg2) << 2

    @insts << x
  end

  def jump_ne(reg1, reg2)
    x = 6 << 4
    x |= reg_no(reg1)
    x |= reg_no(reg2) << 2

    @insts << x
  end


  def add(reg, value)
    if value.is_a? Symbol
      x = 7 << 4

      x |= reg_no(reg)
      x |= reg_no(value) << 2

      @insts << x
    else
      x = 3 << 4
      x |= reg_no(reg)

      @insts << x
      @insts << (value & 0xff)
      @insts << (value >> 8)
    end
  end

  def mult(reg, value)
    x = 5 << 4
    x |= reg_no(reg)

    @insts << x
    @insts << (value & 0xff)
    @insts << (value >> 8)
  end

  def neg(reg)
    x = 4 << 4
    x |= reg_no(reg)
    @insts << x
  end

  def syscall
    @insts << 0xff
  end

  def print(x)
    set :r1, 1

    x.bytes.each do |x|
      set :r2, x
      syscall
    end
  end

  def print_random(x)
    set :r1, 1

    x.bytes.each do |x|
      if x % 2 == 0
        x = (~x) & 0xff
        set :r2, x
        neg :r2
      else
        n = rand(120)
        x = (x - n) & 0xff

        set :r2, x
        add :r2, n
      end

      syscall
    end
  end

  def evaluate(&block)
    instance_eval(&block)
    self
  end

  def getchar
    set :r1, 0
    syscall
  end

  def quit(code = 0)
    set :r1, 2
    set :r2, code

    syscall
  end

  def jump
    @insts << (6 << 4)
  end

  def compile
    @insts.map do |x|
      if x.is_a? Symbol
        @symbols[x].chr
      else
        x.chr
      end
    end.join
  end

  def check_char(c)
    x = rand(3)

    if x == 0
      set :r3, 0xffff - (c & 0xffff) + 1
      add :r1, :r3

    elsif x == 1
      n1 = rand(100) + 30
      n2 = rand(100) + 30

      set :r3, n1
      add :r3, n2

      add :r1, :r3
      neg :r1
      add :r1, n1 + n2 + c + 1
    else
      n1 = rand(100) + 2
      n2 = rand(100) + 2

      mult :r1, n1
      set :r3, n2
      add :r1, :r3
      add :r1, 0xffff - ((c * n1 + n2) & 0xffff) + 1
    end
  end
end

password = "DCI{m4ke_m0ar_gr3at_languages}".bytes

p = Program.new.evaluate do
  set :r1, 1
  set :r2, 204
  jump

  _good = ip
  print_random "Good password\n"
  quit(0)

  _wrong = ip
  print_random "Wrong password\n"
  quit(1)

  # 194
  print_random "Enter password: "

  set :r4, 0

  password.each do |c|
    getchar

    check_char(c)

    add :r4, :r1
  end

  mov :r1, :r4
  set :r2, _wrong
  jump


  set :r1, 1
  set :r2, _good
  jump
end

print p.compile
