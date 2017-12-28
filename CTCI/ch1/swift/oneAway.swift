func lengthDifference(string1 : String, string2 : String) -> Int {
    let s1Length : Int = string1.characters.count;
    let s2Length : Int = string2.characters.count;
    let diff : Int = s1Length - s2Length;
    return diff < 0 ? diff * -1 : diff;
}

func checkEdits(s1 : String, s2 : String) -> Int {
    var x : Int = 0;
    var y : Int = 0;
    var editsMade : Int = 0;
    let s1Chars : [Character] = [Character](s1.characters);
    let s2Chars : [Character] = [Character](s2.characters);
    while(x < s1.characters.count && y < s2.characters.count){
        if(s1Chars[x] != s2Chars[y]){
            editsMade+=1;
            x+=1;
        } else {
            x+=1;
            y+=1;
        }
    }
    return editsMade;
}

func oneAway(string1 : String, string2 : String) -> Bool {
    let diff : Int = lengthDifference(string1: string1, string2: string2);
    let s1Chars : [Character] = [Character](string1.characters);
    let s2Chars : [Character] = [Character](string2.characters);
    var editsMade : Int = 0;
    if(diff > 1) {
        return false;
    }
    else if(diff == 0){
        for i : Int in 0 ..< string1.characters.count {
            if(s1Chars[i] != s2Chars[i]){
                editsMade+=1;
            }
        }
    }
    else if(diff == 1){
        if(s1Chars.count > s2Chars.count){
            editsMade = checkEdits(s1: string1, s2: string2);
        } else {
           editsMade = checkEdits(s1: string2, s2: string1)
        }
    }
    
    if editsMade > 1{
        return false;
    }
    return true;
}


print(oneAway(string1: "pale", string2: "ple"));
print(oneAway(string1: "pales", string2: "pale"));
print(oneAway(string1: "pale", string2: "bale"));
print(oneAway(string1: "pale", string2: "bake"));
print(oneAway(string1: "pizza", string2: "italy"));
print(oneAway(string1: "bus", string2: "backpack"));


/*
    > swift oneAway.swift

    prints:
        > True
        > True
        > True
        > False
        > False
        > False
*/