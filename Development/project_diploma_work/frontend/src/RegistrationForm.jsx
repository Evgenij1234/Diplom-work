import React, { useState, useRef, useEffect } from "react";

function RegistrationForm({isFormVisible}) {
  if(isFormVisible === false){
    return null;
  }
  else{
    return( 
    <div className="RegistrationForm">
         
    </div>
    );
  }
}

export default RegistrationForm;
