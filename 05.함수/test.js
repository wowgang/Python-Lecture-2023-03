function facto(num) {
    if (num == 0)
        return 1;
    return num * facto(num -1);
}
console.log(facto(5));