#!/usr/bin/node
exports.esrever = function (list) {
    if (list.length <= 1) {
        return list;
      }
      return esrever(list.slice(1)).concat(list[0]);
}
