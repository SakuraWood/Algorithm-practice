var singleNumber = function(nums) {
    var k, bitCount, i, j, n, hasBit, exept;
    k = 3;
    bitCount = [];
    for (i = 0; i < 32; i++) {
        bitCount[i] = 0;
    }
    for (j = 0; j < nums.length; j++) {
        n = nums[j];
        for (i = 0; i < 32; i++) {
            hasBit = (n & (1 << i)) !== 0;
            if (hasBit) {
                bitCount[i] = (bitCount[i] + 1) % k;
            }
        }
    }
    exept = 0;
    for (i = 0; i < 32; i++) {
      if (bitCount[i] > 0) {
        exept |= (1 << i);
      }
    }
    return exept;
}

var nums=[3,1,3,3,2,2,2];
console.log(singleNumber(nums));

