<?php

class Path {

    // Constants
    const SEPARATOR = '/';
    const PATH_PARENT = '..';
    const PATH_SAME = '.';

    // I keep the current dir in an array
    private $stack;

    // The constructor
    public function __construct($path = '/'){
        $this->stack = [];
        $this->cd($path);
    }

    // Change directory method
    public function cd($path){

        // Divide the path into this components
        $parts = explode(self::SEPARATOR, $path);

        // Check if this is an absolute path
        if(empty($parts[0])){

            // Reset the stack
            $this->stack = [];
            array_shift($parts);
        }

        // Iterate over the components
        foreach($parts as $part){

            // Do nothing
            if($part === self::PATH_SAME) continue;

            // Go up the tree
            if($part === self::PATH_PARENT){

                // Parent of the root?? Where are you going??
                if(empty($this->stack)){
                    throw new \Error("You are already at the root");
                }

                // Go to the parent
                array_pop($this->stack); 
                continue;
            };

            // Add the path
            // TODO: Check it's a-zA-Z
            if(empty($part)) continue;
            $this->stack[] = $part;

        }


    } // cd
    

    // Magic methods!!
    function __get (string $name){
        if($name === 'currentPath')
            return $this->getCurrentPath();
    }

    // This is the method that returns the current path
    public function getCurrentPath(){
        return self::SEPARATOR . implode(self::SEPARATOR, $this->stack);
    }

}