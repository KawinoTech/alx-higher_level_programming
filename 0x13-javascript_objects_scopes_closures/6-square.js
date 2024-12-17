#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0)
        {
            this.width = w;
            this.height = h;
        }
    }

    print () {
        let buffer = ""
        for (let i = 0; i < this.height; i++)
        {
            for (let j = 0; j < this.width; j++)
            {
                buffer += "#";
            }
            if (i < this.height - 1)
            {
                buffer += "\n";
            }
        }
        console.log(buffer)
    }
    double () {
        for (let attr_key in this) {
            this[attr_key] = 2 * this[attr_key]
        }
    }
    rotate () {
        let height = this.height;
        this.height = this.width;
        this.width = height;
    }
}

class Square extends Rectangle {
    constructor (size) {
        super(size, size)
    }
    charPrint(c) {
        if (!c) {
            super.print();
        }
        else {
            let buffer = ""
            for (let i = 0; i < this.height; i++)
            {
                for (let j = 0; j < this.width; j++)
                {
                    buffer += c;
                }
                if (i < this.height - 1)
                {
                    buffer += "\n";
                }
            }
            console.log(buffer)
        }
    }
}
