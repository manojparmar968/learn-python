import React, { Component } from 'react'
import { Text, View } from 'react-native'

export function handleValidation(text, type){
    console.log("texttype==>>",text, type)

    if(type === 'name') {
        var nameRegex = /([A-z][\s\.]|[A-z])+$/;
        text = text.trim();
        if (text == "" || text == undefined || text == null) {
            return { status: false, value:text , error: "Please enter name." };
        }
        else if (!nameRegex.test(text)) {
            return { status: false, error: "Please enter valid name." };
        }
        else {
            return { status: true, error: '',};
        }
    }

    else if(type === 'last'){
        var lastRegex = /([A-z][\s\.]|[A-z])+$/;
        last = last.trim();
        if (last == "" || last == undefined || last == null) {
            return { status: false, value:text , error: "Please enter last name." };
        }
        else if (!lastRegex.test(last)) {
            return { status: false, error: "Please enter valid last name." };
        }
        else {
            return { status: true, error: '',height: 0 };
        } 
    }

    else if(type === 'email'){
        var emailRegex = /^[A-Z0-9_-]+([\.][A-Z0-9_]+)*@[A-Z0-9-]+(\.[a-zA-Z]{2,3})+$/i;
        text = text.trim();
        if (text == "" || text == undefined || text == null) {
            return { status: false, value:text , error: "Please enter Email ID." };
        }
        else if (!emailRegex.test(text)) {
            return { status: false, error: "Please enter valid Email Address." };
        }
        else {
            return { status: true, error: '',height: 0 };
        }
    }

    else if(type === 'password'){
        //var passwordRegex = /^ (?=^.{8,16}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/;
       // var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        text = text.trim();

        if (text == "" || text == undefined || text == null) {
            return { status: false, value:text , error: "Please enter valid password." }
        } 
        // else if (!passwordRegex.test(text)) {
        //     return { status: false, error: "Please enter valid password." };
        // }
        // else if (password.length < 6) {
        //     return { status: false, error: "Password must contain 6 or more than 6 characters." };
        // }
        else {
            return { status: true, error: '',height: 0 }
        }
    }

    else if(type === 'mobileNo'){
        var numberRegex = /^[1-9][0-9]{9,12}$/;
        text = text.trim()
        if (text == "" || text == undefined || text == null) {
            return { status: false, value:text , error: "Please enter mobileNo." }
        }else if(!numberRegex.test(text)){
            return { status: false, error: "Please enter valid mobileNo." }
        }else {
            return { status: true, error: '',height: 0 }
        }
    }
    
}



/* To handle first name validation*/
export function validateName(name) {
    var nameRegex = /([A-z][\s\.]|[A-z])+$/;
    name = name.trim();
    if (name == "" || name == undefined || name == null) {
        return { status: false, error: "Please enter name." };
    }
    else if (!nameRegex.test(name)) {
        return { status: false, error: "Please enter valid name." };
    }
    else {
        return { status: true, error: '',height: 0 };
    }
}
 
/* To handle last name validation*/
export function validateLastName(last) {
    var lastRegex = /([A-z][\s\.]|[A-z])+$/;
    last = last.trim();
    if (last == "" || last == undefined || last == null) {
        return { status: false, error: "Please enter last name." };
    }
    else if (!lastRegex.test(last)) {
        return { status: false, error: "Please enter valid last name." };
    }
    else {
        return { status: true, error: '',height: 0 };
    }
}

/* To handle email validation */
export function validateEmail(email) {
     var emailRegex = /^[A-Z0-9_-]+([\.][A-Z0-9_]+)*@[A-Z0-9-]+(\.[a-zA-Z]{2,3})+$/i;
    email = email.trim();
    if (email == "" || email == undefined || email == null) {
        return { status: false, error: "Please enter Email ID." };
    }
    else if (!emailRegex.test(email)) {
        return { status: false, error: "Please enter valid Email Address." };
    }
    else {
        return { status: true, error: '',height: 0 };
    }
}
/* To validate password */

export function validatePassword(password) {
    var passwordRegex = /^ (?=^.{8,16}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/;
    password = password.trim();

    if (password == "" || password == undefined || password == null) {
        return { status: false, error: "Please enter valid password." }
    } 
    // else if (!passwordRegex.test(password)) {
    //     return { status: false, error: "Please enter valid password." };
    // }
    else if (password.length < 6) {
        return { status: false, error: "Password must contain 6 or more than 6 characters." };
    }
    else {
        return { status: true, error: '',height: 0 }
    }
}

/* To validate Mobile No. */

export function validateMobileNo(mobileNo) {
    var numberRegex = /^[1-9][0-9]{9,12}$/;
    mobileNo = mobileNo.trim()
    if (mobileNo == "" || mobileNo == undefined || mobileNo == null) {
        return { status: false, error: "Please enter mobileNo." }
    }else if(!numberRegex.test(mobileNo)){
        return { status: false, error: "Please enter valid mobileNo." }
    }else {
        return { status: true, error: '',height: 0 }
    }
}


