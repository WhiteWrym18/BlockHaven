// // src/main.ts
//console.log("Hello from TypeScript!");

// //src/main.ts
//import { World } from './world';
//import { Player } from './player';
//*const canvas = document.getElementById('gameCanvas') as HTMLCanvasElement;
//const ctx = canvas.getContext('2d')

//if (!ctx) {
    //console.error("Could not get 2D rendering context!")
//} else {
    //console.error("Canvas context obtained!")

    // // Set the canvas dimensions to fill the browser window
    //canvas.width = window.innerWidth;
    //canvas.height = window.innerHeight;

    //const worldWidth = 30; // Number of blocks wide
    //const worldHeight = 20; // Number of blocks high
    //const blockSize = 20; // Size of each block in pixels
    
    //const world = new World(worldWidth, worldHeight);

    //function drawWorld() {
        //if (!ctx) return;
        //ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas

        //for (let y = 0; y < world.height; y++) {
            //for (let x = 0; x < world.width; x++) {
                //const block = world.getBlock(x, y);
                //if (block) {
                    //let color = '';
                    //switch (block) {
                        //case 'grass':
                            //color = 'green';
                            //break;
                        //case 'dirt':
                            //color = 'brown';
                            //break;
                        //case 'stone':
                            //color = 'gray';
                            //break;
                    //}
                    //ctx.fillStyle = color;
                    //ctx.fillRect(x * blockSize, y * blockSize, blockSize, blockSize);
                    //ctx.strokeStyle = 'black'; // Add a border for better visibility
                    //ctx.strokeRect(x * blockSize, y * blockSize, blockSize, blockSize);
                //}
            //}
        //}
    //}

    //const playerSize = blockSize;
    //const playerStartX = blockSize * 2;
    //const playerStartY = (worldHeight - 6) * blockSize; // Start on the grass
    //const player = new Player(playerStartX, playerStartY, playerSize, 'yellow');

    //function drawPlayer() {
        //player.draw(ctx);
    //}
    
    function gameLoop() {
        if (!ctx) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawWorld();
        drawPlayer();
        requestAnimationFrame(gameLoop); // Loop for smooth animation
    }

    const playerSpeed = 5;

    document.addEventListener('keydown', (event) => {
        switch (event.key) {
            case 'ArrowLeft':
                player.move(-playerSpeed, 0);
                break;
            case 'ArrowRight':
                player.move(playerSpeed, 0);
                break;
            case 'ArrowUp':
                player.move(0, -playerSpeed);
                break;
            case 'ArrowDown':
                player.move(0, playerSpeed);
                break;
        }
    });

    gameLoop(); // Start the game loop
}