 // // src/world.ts
//export type BlockType = 'grass' | 'dirt' | 'stone';

//export class World {
    //private grid: BlockType[][];
    //public readonly width: number;
    //public readonly height: number;

    //constructor(width: number, height: number) {
        //this.width = width;
        //this.height = height;
        //this.grid = [];
        //this.generateWorld();
    //}

    //private generateWorld(): void {
        //for (let y = 0; y < this.height; y++) {
            //this.grid[y] = [];
            //for (let x = 0; x < this.width; x++) {
                //if (y < this.height - 5) {
                    //this.grid[y][x] = 'grass';
                //} else if (y < this.height - 1) {
                    //this.grid[y][x] = 'dirt';
                //} else {
                    //this.grid[y][x] = 'stone';
                //}
            //}
        //}
    //}

    public getBlock(x: number, y: number): BlockType | undefined {
        if (y >= 0 && y < this.height && x >= 0 && x < this.width) {
            return this.grid[y][x];
        }
        return undefined;
    }

    public setBlock(x: number, y: number, type: BlockType): void {
        if (y >= 0 && y < this.height && x >= 0 && x < this.width) {
            this.grid[y][x] = type;
        }
    }
}