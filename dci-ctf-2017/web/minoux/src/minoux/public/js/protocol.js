function protocol(str) {
    this.index = 0;

    this.parse = function() {
        if(str[this.index] == ':') {
            this.index++;
            this.parseInteger();
        } else if(str[this.index] == '$') {
            this.index++;
            this.parseString();
        } else if(str[this.index] == '*') {
            this.index++;
            this.parseArray();
        }

        return this.value;
    };

    this.parseInteger = function() {
        var endLine = str.slice(this.index).indexOf("\r\n");
        this.value = +str.slice(this.index).substr(0, str.slice(this.index).indexOf("\r\n"));
        this.index += endLine + 2;
    };

    this.parseString = function() {
        var endLine = str.slice(this.index).indexOf("\r\n");
        var length = +str.slice(this.index).substr(0, str.slice(this.index).indexOf("\r\n"));

        this.index += endLine + 2;
        this.value = str.substr(this.index, length);
        this.index += length + 2;
    };

    this.parseArray = function() {
        var endLine = str.slice(this.index).indexOf("\r\n");
        var length = +str.slice(this.index).substr(0, str.slice(this.index).indexOf("\r\n"));
        var output = [];

        this.index += endLine + 2;

        for(var i = 0; i < length; i++) {
            this.parse();
            output.push(this.value);
        }

        this.value = output;
    };
}


