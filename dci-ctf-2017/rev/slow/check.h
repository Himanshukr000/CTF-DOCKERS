int v0 = 547;
int v1 = 542;
int v2 = 577;
int v3 = 980;
int v4 = 943;
int v5 = 434;
int v6 = 909;
int v7 = 952;
int v8 = 819;
int v9 = 742;
int v10 = 897;
int v11 = 868;
int v12 = 447;
int v13 = 722;
int v14 = 397;
int v15 = 896;
int v16 = 931;
int v17 = 990;

void send_flag() {
  Serial.print((char)((v0 ^ 3) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v1 ^ 6) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v2 ^ 9) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v3 ^ 12) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v4 ^ 15) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v5 ^ 18) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v6 ^ 21) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v7 ^ 24) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v8 ^ 27) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v9 ^ 30) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v10 ^ 33) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v11 ^ 36) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v12 ^ 39) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v13 ^ 42) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v14 ^ 45) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v15 ^ 48) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v16 ^ 51) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.print((char)((v17 ^ 54) >> 3));
  for(int i = 0; i < 3600; i++) {
    for(int j = 0; j < 24; j++) {
       delay(1000);
    }
  }
  Serial.println();
}
