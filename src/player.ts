// // src/player.ts
// export class Player {
    //public x: number;
    //public y: number;
    //public size: number;
    //public color: string;

    //constructor(x: number, y: number, size: number, color: string) {
        //this.x = x;
        //this.y = y;
        //this.size = size;
        //this.color = color;
    //}

    public move(dx: number, dy: number): void {
        this.x += dx;
        this.y += dy;
    }

    public draw(ctx: CanvasRenderingContext2D | null): void {
        if (ctx) {
            ctx.fillStyle = this.color;
            ctx.fillRect(this.x, this.y, this.size, this.size);
        }
    }
}