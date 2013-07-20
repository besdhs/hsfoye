// JavaScript Document


  function ReceivedFocus(ctl)
  {
    if (ctl.value=="Search"  || ctl.value=="Enter E-mail Address")
    {
    ctl.value="";
    }
  }
  function LostFocus(ctl,message)
  {
		
    if (ctl.value == "")
    {
    ctl.value=message;
    }
  }
