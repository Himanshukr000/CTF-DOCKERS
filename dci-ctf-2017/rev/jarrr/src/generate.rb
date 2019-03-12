require 'prime'

flag = "DCI{jarr_jarr_tell_me_who_wrote_the_worst_java_jar_out_of_all_these_jars}".bytes

$charset = ('a'..'z').to_a

def generate(i)
  x = i + 1

  27.times do
    x = (x * i + i) % 26
  end

  x
end

def create_name(index, length=20)
  length.times.map { |i| $charset[generate(index | i << 4)] }.join.capitalize
end


def create_class(value, index)
  name = create_name(index)

  factors = value.prime_division

  static_vars = factors.map.with_index { |(b, p), i|
    %Q{  public static Integer b#{i} = #{b};
 }
  }.join("\n")

  n = factors.size

  add_factors = factors.flat_map.with_index { |(b, p), i|
    p.times.map {
      "    v *= b#{i};"
    }
  }.shuffle.join("\n")

  code = %Q{
public class #{name} {
#{static_vars}
  public static Integer check(Integer x) {
    Integer v = 1;
#{add_factors}
    return x ^ v;
  }
}
}

  [name, code]
end

mapping = []

flag.each.with_index do |byte, index|
  name, code = create_class(byte, index)

  mapping << name

  File.write("src/#{name}.java", code)
end

ordering = flag.size.times.to_a.shuffle

cases = mapping.map.with_index { |name, i| "      case #{i}: return #{name}.class;"  }.join("\n")

jarrr_code = %Q{
import java.lang.reflect.*;

public class Jarrr {
  public static Integer[] o = new Integer[] {#{ordering.join(',')}};

  public static void main(String args[]) throws Throwable {
    String password = args[0];

    if(password.length() != #{flag.size}) {
      return;
    }

    Integer ok = 0;

    for(Integer i = 0; i < o.length; i++) {
      Class c = Class.forName(cls(i));
      Method m = c.getMethod("check", Integer.class);
      ok += (Integer)m.invoke(null, (Integer)Character.codePointAt(password, i));
    }

    if(ok == 0) {
      System.out.println("Good password");
    } else {
      System.out.println("Bad password");
    }
  }

  public static String cls(Integer i) {
    String n = "";

    for(int j = 0; j < 20; j++) {
      n += Character.toString((char)(c(j) + d(i | j << 4)));
    }

    return n;
  }

  public static Integer d(Integer i) {
    Integer x = i + 1;

    for(int j = 0; j < 27; j++) {
      x = (x * i + i) % 26;
    }

    return x;
  }

  public static Integer c(Integer i) {
    return i == 0 ? 65 : 97;
  }
}
}

File.write('src/Jarrr.java', jarrr_code)

classpath = (["Jarrr.jar"] + mapping.shuffle.map { |x| "#{x}.jar" }).join(':')

File.write('src/run.sh', "java -cp '#{classpath}' Jarrr $@")
