/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    function flatten(arr,curr){
        let result=[];
        for (let item of arr){
            if (Array.isArray(item)&& curr < n){
                result.push(...flatten(item,curr+1));
            }
            else {
                result.push (item);
            }
        }
        return result 
    }
return flatten(arr,0)

};