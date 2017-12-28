func URLify(inputString : String, stringSize : Int) -> String {
    var newString : String = "";
    for letter in inputString.characters {
        if(letter == " "){
            newString+="%20";
        } else {
            newString+=String(letter);
        }
        
    }
    return newString;
}

let string1 : String = "Mr John Smith";
print(URLify(inputString: string1, stringSize: 13));

/*
	> swift URLify.swift

	prints:
		> Mr%20John%20Smith
*/