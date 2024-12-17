exports.nbOccurences = function (list, searchElement) {
    let i = 0;
    let no_of_occurences = 0;
    while( i < list.length) {
        if (list[i] === searchElement) {
            no_of_occurences++;
        }
        i++;
    }
    return no_of_occurences;
}
