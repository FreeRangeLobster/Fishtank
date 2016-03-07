 webiopi().ready(function() {
                        webiopi().setFunction(17,"out");
                        
                        var content, button;
                        content = $("#content");
                        
                        button = webiopi().createGPIOButton(17,"My LED");
                        content.append(button);
                        
                        
        });