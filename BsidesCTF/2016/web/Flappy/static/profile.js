/**
 * Changelog:
 * - Added game over screen
 * - Flappy bird can now fly up above the screen but will still die to obstacles
 * - Flappy bird can no longer go underground
 * - Added alternate control for "flapping". Which would be the space key.
 * - Flappy bird now flaps a whole pixel lower.
 * 
 * TODO: Save your best score
 * TODO: Add scores page
 * 
 **/

var keys = [1];

var count = 0;
var tick = 0;

var score = 0;

var deathTicks = 0;

var buttons = [1];
var gameState = 0; //0 = main-menu, 1 = game, (2 = game over)

var objects = [1];

var started = false;

var keyPressed = function() {
    keys[keyCode] = false;
};
var keyReleased = function() {
    keys[keyCode] = true;
};

var addButton = function(id, state, x, y, width, height, text) {
    var button = {};
    
    button.id = id;
    button.state = state;
    button.x = x;
    button.y = y;
    button.width = width;
    button.height = height;
    button.text = text;
    button.pressed = false;
    
    buttons.push(button);
};

var FlappyBird = function() {
    this.x = 100;
    this.y = 150;
    
    this.descentSpeed = 10;
    
    this.height = 0;
    this.heightIncrement = 0.25;
    
    this.dead = false;
    
    this.draw = function() {
        pushMatrix(); {
            var x = this.x + 16;
            var y = this.y + 12;
            
            var angle = max(-20, (this.descentSpeed - 10) * 4.1);
            if(angle <= 0) {
                
            }
            
            translate(x, y);
            rotate(angle);
            scale(0.80);
            translate(-x, -y);
            
            translate(this.x, this.y);
            this.drawSprite();
        } popMatrix();
    };
    
    this.drawSprite = function() {
        noStroke();
        
        fill(255, 255, 255);
        rect(2, 8, 10, 8);
        rect(8, 4, 4, 2);
        rect(12, 2, 6, 2);
        rect(16, 2, 10, 10);
        rect(26, 4, 4, 10);
        
        fill(23, 23, 23);
        rect(0, 8, 2, 2);
        rect(0, 10, 2, 2);
        rect(0, 12, 2, 2);
        rect(2, 6, 2, 2);
        rect(2, 14, 2, 2);
        rect(4, 6, 2, 2);
        rect(4, 16, 2, 2);
        rect(4, 18, 2, 2);
        rect(6, 4, 2, 2);
        rect(6, 6, 2, 2);
        rect(6, 16, 2, 2);
        rect(6, 20, 2, 2);
        rect(8, 2, 2, 2);
        rect(8, 6, 2, 2);
        rect(8, 16, 2, 2);
        rect(8, 20, 2, 2);
        rect(10, 2, 2, 2);
        rect(10, 8, 2, 2);
        rect(10, 14, 2, 2);
        rect(10, 22, 2, 2);
        rect(12, 0, 2, 2);
        rect(12, 10, 2, 2);
        rect(12, 12, 2, 2);
        rect(12, 22, 2, 2);
        rect(14, 0, 2, 2);
        rect(14, 22, 2, 2);
        rect(16, 0, 2, 2);
        rect(16, 4, 2, 2);
        rect(16, 6, 2, 2);
        rect(16, 8, 2, 2);
        rect(16, 16, 2, 2);
        rect(16, 22, 2, 2);
        rect(18, 0, 2, 2);
        rect(18, 2, 2, 2);
        rect(18, 10, 2, 2);
        rect(18, 14, 2, 2);
        rect(18, 18, 2, 2);
        rect(18, 22, 2, 2);
        rect(20, 0, 2, 2);
        rect(20, 12, 2, 2);
        rect(20, 16, 2, 2);
        rect(20, 20, 2, 2);
        rect(22, 0, 2, 2);
        rect(22, 12, 2, 2);
        rect(22, 16, 2, 2);
        rect(22, 20, 2, 2);
        rect(24, 0, 2, 2);
        rect(24, 12, 2, 2);
        rect(24, 16, 2, 2);
        rect(24, 20, 2, 2);
        rect(26, 2, 2, 2);
        rect(26, 6, 2, 2);
        rect(26, 8, 2, 2);
        rect(26, 12, 2, 2);
        rect(26, 16, 2, 2);
        rect(26, 20, 2, 2);
        rect(28, 4, 2, 2);
        rect(28, 12, 2, 2);
        rect(28, 16, 2, 2);
        rect(28, 20, 2, 2);
        rect(30, 6, 2, 2);
        rect(30, 8, 2, 2);
        rect(30, 10, 2, 2);
        rect(30, 12, 2, 2);
        rect(30, 16, 2, 2);
        rect(30, 20, 2, 2);
        rect(32, 12, 2, 2);
        rect(32, 16, 2, 2);
        rect(32, 18, 2, 2);
        rect(34, 14, 2, 2);
        
        fill(247, 255, 0);
        rect(2, 12, 2, 2);
        rect(4, 14, 2, 2);
        rect(6, 14, 2, 2);
        rect(8, 14, 2, 2);
        rect(10, 6, 2, 2);
        rect(10, 12, 2, 2);
        rect(12, 4, 2, 2);
        rect(12, 6, 2, 2);
        rect(12, 8, 2, 2);
        rect(12, 14, 2, 2);
        rect(14, 4, 2, 12);
        rect(16, 10, 2, 6);
        rect(18, 12, 2, 2);
        
        fill(244, 202, 22);
        rect(6, 18, 2, 2);
        rect(8, 18, 2, 2);
        rect(10, 16, 6, 6);
        rect(16, 18, 2, 4);
        rect(18, 20, 2, 2);
        
        fill(214, 43, 43);
        rect(18, 16, 2, 2);
        rect(20, 14, 14, 2);
        rect(20, 18, 12, 2);
    };
    
    this.update = function() {
        if(gameState === 1 && started) {
            this.controls();
        
            this.y += this.descentSpeed;
            
            this.descentSpeed += 1.25;
        } else if(gameState === 1) {
            this.y += this.height;
            
            this.height += this.heightIncrement;
            if(abs(this.height) >= 1.25) {
                this.heightIncrement *= -1;
            }
        }
        
        if(this.dead) {
            this.descentSpeed = min(32, this.descentSpeed + 2.0);
            
            this.y += 12;
            
            deathTicks++;
            
            if(this.y >= 332) {
                this.y = 332;
            }
            
            if(deathTicks === 15) {
                addButton(0, 2, 135, 310, 130, 38, "PLAY AGAIN");
            }
        }
    };
    
    this.controls = function() {
        if((mouseIsPressed || keys[32]) && !this.dead) {
            this.descentSpeed = -7;
        }
    };
};
var FlappiestBird = new FlappyBird();

var initProgram = function() {
    buttons = [];
    
    addButton(0, 0, 50, 290, 130, 38, "START");
    addButton(1, 0, 220, 290, 130, 38, "SCORES");
    
    score = 0;
    deathTicks = 0;
    
    count = 0;
    tick = 0;
    
    gameState = 0;
    objects = [];
    started = false;
    
    FlappiestBird = new FlappyBird();
};
initProgram();

var buttonPressed = function(button) {
    switch(button.state) {
        case 0:
            switch(button.id) {
                case 0:
                    gameState = 1;
                    score = 0;
                    started = false;
                    break;
                default:
                    break;
            }
            break;
        case 2:
            switch(button.id) {
                case 0:
                    initProgram();
                    break;
                default:
                    break;
            }
            break;
        default:
            break;
    }
};

var addObject = function() {
    var lastY = random(20) + 150;
    
    if(objects.length > 0) {
        var lastObject = objects[objects.length - 1];
        lastY = lastObject.y;
    }
    
    var object = {};
    
    object.y = max(90, min(260, lastY + random(200) - 100));
    object.x = 450;
    
    objects.push(object);
};

var drawPixelatedEllipse = function(x, y, width, height, colour) {
    fill(colour);
    ellipse(x, y, width, height);
    
    noStroke();
    fill(red(colour) + 10, green(colour) + 10, blue(colour) + 10);
    for(var i = 0; i <= 360; i += 7) {
        var xx = x + cos(i) * (width / 2);
        var yy = y + sin(i) * (height / 2);
        
        rect(xx - 3, yy - 3, 6, 6);
    }
};

var mousePressed = function() {
    if(gameState === 1) {
        if(!started) {
            started = true;
        }
    }
    
    for(var i = 0; i < buttons.length; i++) {
        var button = buttons[i];
        
        if(button.state === gameState) {
            if(mouseX >= button.x - 1 && mouseX <= button.x + button.width + 1 && 
                mouseY >= button.y - 1 && mouseY <= button.y + button.height + 1) {
                buttonPressed(button);
            }
        }
    }
};

var die = function() {
    FlappiestBird.dead = true;
    gameState = 2;
    deathTicks = 0;
};

var intersects = function(r1, r2) {
    return !(r2.left >= r1.right || 
           r2.right <= r1.left || 
           r2.top >= r1.bottom ||
           r2.bottom <= r1.top);
};

draw = function() {
    background(91, 199, 199);
    
    if(gameState !== 2) {
        count += 3;
        if(count >= 15) {
            count = 0;
        }
    }
    
    pushMatrix();
    
    translate(200, 200);
    scale((deathTicks > 0 && deathTicks <= 10)? 1.01 : 1.0);
    translate(-200, -200);
    
    if(deathTicks > 0 && deathTicks <= 10) {
        translate(random(4) - 2, random(4) - 2);
    }
    //Draw background
    noStroke();
    
    fill(255, 255, 255);
    drawPixelatedEllipse(20, 320, 80, 80, color(255, 255, 255));
    drawPixelatedEllipse(70, 340, 80, 80, color(255, 255, 255));
    drawPixelatedEllipse(115, 325, 80, 75, color(255, 255, 255));
    drawPixelatedEllipse(160, 330, 50, 60, color(255, 255, 255));
    drawPixelatedEllipse(200, 320, 60, 60, color(255, 255, 255));
    drawPixelatedEllipse(240, 325, 60, 80, color(255, 255, 255));
    drawPixelatedEllipse(270, 335, 60, 80, color(255, 255, 255));
    drawPixelatedEllipse(310, 330, 60, 60, color(255, 255, 255));
    drawPixelatedEllipse(350, 325, 50, 60, color(255, 255, 255));
    drawPixelatedEllipse(390, 320, 70, 80, color(255, 255, 255));
    
    drawPixelatedEllipse(112, 370, 76, 76, color(29, 196, 79));
    drawPixelatedEllipse(251, 378, 83, 90, color(29, 196, 79));
    drawPixelatedEllipse(0, 367, 74, 89, color(29, 196, 79));
    drawPixelatedEllipse(350, 368, 73, 60, color(29, 196, 79));
    drawPixelatedEllipse(140, 376, 72, 71, color(29, 196, 79));
    drawPixelatedEllipse(434, 353, 70, 85, color(29, 196, 79));
    drawPixelatedEllipse(207, 380, 77, 86, color(29, 196, 79));
    drawPixelatedEllipse(320, 373, 73, 84, color(29, 196, 79));
    drawPixelatedEllipse(82, 372, 75, 73, color(29, 196, 79));
    drawPixelatedEllipse(221, 380, 77, 84, color(29, 196, 79));
    drawPixelatedEllipse(388, 375, 77, 72, color(29, 196, 79));
    drawPixelatedEllipse(273, 380, 90, 75, color(29, 196, 79));
    drawPixelatedEllipse(404, 388, 88, 88, color(29, 196, 79));
    drawPixelatedEllipse(176, 378, 85, 79, color(29, 196, 79));
    drawPixelatedEllipse(86, 368, 81, 83, color(29, 196, 79));
    drawPixelatedEllipse(293, 378, 88, 90, color(29, 196, 79));
    drawPixelatedEllipse(52, 376, 84, 84, color(29, 196, 79));
    drawPixelatedEllipse(24, 376, 74, 81, color(29, 196, 79));
    
    if(gameState === 1 || gameState === 2) {
        if(!FlappiestBird.dead) {
            if(FlappiestBird.y >= 320) {
                die();
            }
        }
        var playerAABB = {};
        
        playerAABB.left = FlappiestBird.x;
        playerAABB.right = FlappiestBird.x + 34;
        playerAABB.top = FlappiestBird.y;
        playerAABB.bottom = FlappiestBird.y + 24;
        
        //Draw obstacles
        var index = objects.length;
        while(index--) {
            var object = objects[index];
            
            object.x -= FlappiestBird.dead? 0 : 3;
            
            var topAABB = {};
            
            topAABB.left = object.x - 5;
            topAABB.right = object.x + 45;
            topAABB.top = -5000;
            topAABB.bottom = object.y - 55;
            
            var bottomAABB = {};
            
            bottomAABB.left = object.x - 5;
            bottomAABB.right = object.x + 45;
            bottomAABB.top = object.y + 38;
            bottomAABB.bottom = 300;
            
            if(abs(object.x - FlappiestBird.x) <= 1) {
                score++;
            }
            
            if(intersects(playerAABB, topAABB) || intersects(playerAABB, bottomAABB)) {
                die();
            }
            
            pushMatrix(); {
                translate(0, -10);
                
                strokeWeight(2);
                stroke(0, 0, 0);
                
                fill(56, 207, 39);
                
                rect(object.x, -2, 40, object.y - 50);
                rect(object.x - 5, object.y - 70, 50, 25);
                
                noStroke();
                
                fill(255, 255, 255, 100);
                
                rect(object.x, 0, 11, object.y - 71);
                rect(object.x - 4, object.y - 66, 11, 20);
                rect(object.x + 9, object.y - 66, 2, 20);
                rect(object.x + 13, 0, 2, object.y - 71);
                
                fill(255, 255, 255, 150);
                
                rect(object.x + 2.5, 0, 3, object.y - 71);
                rect(object.x - 1.5, object.y - 66, 3, 20);
                
                fill(0, 0, 0, 100);
                
                rect(object.x + 40, 0, -5, object.y - 71);
                rect(object.x + 33, 0, -2, object.y - 71);
                rect(object.x - 4, object.y - 70, 50, 3);
                rect(object.x + 39, object.y - 67, 5, 22);
                rect(object.x + 35, object.y - 67, 2, 22);
                
                fill(0, 0, 0, 50);
                rect(object.x - 4, object.y - 67, 39, 1);
                rect(object.x + 37, object.y - 67, 3, 1);
            } popMatrix();
            
            pushMatrix(); {
                translate(0, 10);
                
                strokeWeight(2);
                stroke(0, 0, 0);
                
                fill(56, 207, 39);
                rect(object.x, object.y + 50, 40, 400);
                rect(object.x - 5, object.y + 30, 50, 25);
                
                noStroke();
                fill(255, 255, 255, 100);
                rect(object.x, object.y + 56, 11, 300);
                rect(object.x + 13, object.y + 56, 2, 300);
                rect(object.x - 4, object.y + 31, 11, 20);
                rect(object.x + 9, object.y + 31, 2, 20);
                
                fill(255, 255, 255, 150);
                rect(object.x + 2.5, object.y + 56, 3, 300);
                rect(object.x - 1.5, object.y + 31, 3, 20);
                
                fill(0, 0, 0, 100);
                rect(object.x + 40, object.y + 56, -5, 300);
                rect(object.x + 33, object.y + 56, -2, 300);
                rect(object.x - 4, object.y + 52, 50, 3);
                rect(object.x + 39, object.y + 30, 5, 22);
                rect(object.x + 35, object.y + 30, 2, 22);
                
                fill(0, 0, 0, 50);
                rect(object.x - 4, object.y + 51, 39, 1);
                rect(object.x + 37, object.y + 51, 3, 1);
            } popMatrix();
            
            if(object.x <= -50) {
                objects.splice(index, 1);
            }
        }
    }
    noStroke();

    
    fill(250, 215, 73);
    rect(0, 360, 400, 40);
    fill(84, 222, 0);
    rect(0, 350, 400, 12);
    fill(255, 255, 255, 200);
    rect(0, 350, 400, 2);
    fill(0, 0, 0);
    rect(0, 349, 400, 1);
    
    fill(0, 0, 0, 40);
    rect(0, 360, 400, 3);
    rect(0, 361, 400, 3);
    rect(0, 362, 400, 3);
    
    fill(124, 242, 0);
    for(var i = 0; i < 30; i++) {
        var x = i * 15 - count;
        quad(x, 352, x + 7, 352, x, 360, x - 7, 360);
    }
    
    tick++;
    if(this.gameState !== 0) {
        FlappiestBird.update();
        FlappiestBird.draw();
    }
    
    popMatrix();
    
    if(gameState === 1) {
        if(started) {
            if(tick % 50 === 0) {
                addObject();
            }
            
            fill(255, 255, 255);
            text(score, 200, 130);
        } else {
            fill(255, 0, 0);
            strokeWeight(2);
            stroke(255, 255, 255);
            
            beginShape();
            vertex(205, 227);
            vertex(213, 220);
            vertex(237, 220);
            vertex(237, 234);
            vertex(213, 234);
            vertex(205, 227);
            endShape();
            
            fill(255, 255, 255);
            textFont(createFont("Monospace", 10), 12);
            text("TAP", 223, 227);
            
            noStroke();
            
            pushMatrix(); {
                translate(-10, 28);
                
                fill(255, 255, 255);
                rect(202, 200, 2, 28);
                rect(200, 218, 2, 8);
                rect(198, 212, 2, 12);
                rect(200, 212, 16, 16);
                rect(206, 208, 6, 4);
                
                fill(0, 0, 0);
                rect(200, 200, 2, 18);
                rect(204, 200, 2, 14);
                rect(202, 198, 2, 2);
                rect(198, 210, 2, 2);
                rect(196, 212, 2, 12);
                rect(198, 224, 2, 2);
                rect(200, 226, 2, 2);
                rect(202, 228, 12, 2);
                rect(206, 206, 2, 2);
                rect(208, 208, 2, 6);
                rect(210, 208, 2, 2);
                rect(212, 210, 4, 2);
                rect(212, 212, 2, 4);
                rect(216, 212, 2, 12);
                rect(214, 224, 2, 4);
            } popMatrix();
            
            stroke(0, 0, 0);
            strokeWeight(1.5);
            
            line(189, 225, 183, 216);
            line(193, 223, 193, 213);
            line(197, 225, 203, 216);
        }
    }
    
    //Draw buttons
    for(var i = 0; i < buttons.length; i++) {
        var button = buttons[i];
        
        if(button.state === gameState) {
            if(mouseX >= button.x - 1 && mouseX <= button.x + button.width + 1 && 
                mouseY >= button.y - 1 && mouseY <= button.y + button.height + 1) {
                button.pressed = true;
            } else {
                button.pressed = false;
            }
            
            //Draw
            stroke(112, 73, 14);
            strokeWeight(2);
            
            fill(255, 255, 255);
            rect(button.x, button.y + (button.pressed? 2 : 0), button.width, button.height);
            
            noStroke();
            fill(209, 101, 30);
            rect(button.x + 3, button.y + 3 + (button.pressed? 2 : 0), button.width - 6, button.height - 6);
            
            fill(255, 255, 255);
            textAlign(CENTER, CENTER);
            textFont("Monospace", 16);
            text(button.text, button.x + button.width / 2, button.y + button.height / 2 + (button.pressed? 2 : 0));
            
            fill(112, 73, 14);
            rect(button.x - 1, button.y + button.height + 1, button.width + 2, 2);
        }
    }
    
    if(gameState === 2) {
        if(deathTicks === 2) {
            noStroke();
            fill(255, 255, 255);
            rect(0, 0, 400, 400);
        }
        if(FlappiestBird.y >= 325 && deathTicks >= 15) {
            strokeWeight(2);
            stroke(0, 0, 0);
            
            fill(222, 213, 146);
            rect(75, 150, 250, 150);
            
            stroke(207, 172, 91);
            fill(222, 216, 151);
            rect(80, 155, 240, 140);
            
            stroke(217, 197, 126);
            rect(81, 156, 238, 138);
            
            fill(242, 232, 172);
            rect(76, 152, 248, 0.1);
            
            fill(196, 153, 72);
            textSize(15);
            
            textAlign(RIGHT, CENTER);
            text("SCORE", 305, 175);
            text("BEST", 305, 225);
            
            fill(255, 255, 255);
            textSize(20);
            
            text(score, 305, 200);
            text(score, 305, 250);
        }
    }
};
