#!/usr/bin/node
let message = "";
if (Object.is(parseInt(process.argv[2]), NaN))
{
    console.log("Missing size");
}
else if (parseInt(process.argv[2]) <= 0);
else
{
    let i = 0;
    while (i < parseInt(process.argv[2]))
    {
        for (let j = 0; j != parseInt(process.argv[2]); j++)
        {
            message += "X";
        }
        if (i < parseInt(process.argv[2]) - 1)
        {
            message += "\n";
        }
        i++;
    }
}
console.log(message);
