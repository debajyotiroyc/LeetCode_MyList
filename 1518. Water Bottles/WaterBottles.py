public int numWaterBottles(int numBottles, int numExchange) {
        int x=numBottles;
        int s=0;
        int k=0;
        while (x>=numExchange){
          k=x%numExchange;
          x=x/numExchange;
          s=s+x;
          x=x+k;
          }
          
        return numBottles+s;
        
    }