rm src/*
ruby generate.rb

cd src/

chmod +x run.sh

javac *.java

for file in *.class; do
    if [ "$file" = "Jarrr.class" ]; then
        jar -cvfm Jarrr.jar ../manifest.txt  Jarrr.class
    else
        jar cf "${file/class/jar}" $file
    fi
done

rm *.java *.class

cd ..

tar -cvf jarrr.tar.gz jarrr
