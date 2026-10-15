#include <math.h>
#include <stdio.h>

/* Learning requirement: closing target AND TTC <= 2 s => warning ON.
   Inputs are ideal target range and relative velocity, not radar raw data. */
int main(void) {
    double range_m, relative_velocity_mps;
    while (scanf("%lf %lf", &range_m, &relative_velocity_mps) == 2) {
        if (!isfinite(range_m) || !isfinite(relative_velocity_mps) || range_m < 0)
            return 2;
        if (relative_velocity_mps >= 0) {
            puts("{\"ttc_s\":null,\"fcw\":\"OFF\"}");
        } else {
            double ttc_s = range_m / -relative_velocity_mps;
            printf("{\"ttc_s\":%.12g,\"fcw\":\"%s\"}\n", ttc_s,
                   ttc_s <= 2.0 ? "ON" : "OFF");
        }
    }
    return feof(stdin) ? 0 : 2;
}
