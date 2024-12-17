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
}
