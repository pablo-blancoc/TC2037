/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.project01;

/**
 *
 * @author Pablo
 */

public class MyHilo extends Thread{
    private int id;
    private boolean flag;
    private int start;
    private int end;
    private long result;
    
    private boolean isPrime(int n) {
        if(n < 2) {
            return false;
        }
        else {
            boolean prime = true;
            for(int i=2; i<=Math.sqrt(n); i++) {
                if(n%i == 0) {
                    prime = false;
                    break;
                }
            }
            return prime;
        }
    }
    
    MyHilo(int id, boolean flag, int start, int end) {
        this.id = id;
        this.flag = flag;
        this.start = start;
        this.end = end;
        this.result = 0;
    }
    
    @Override
    public void run() {
        for(int i=this.start; i<this.end; i++) {
            if(isPrime(i)) {
                this.result += i;
            }
        }
    }
    
    void detener() {
        this.flag = false;
    }
    
    public long getResult() {
        return this.result;
    }
}
