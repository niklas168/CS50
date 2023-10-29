#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // Open the forensic image file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Variables to keep track of file information
    int counter = 0;
    char filename[8];
    FILE *jpeg = NULL;

    // Buffer to read 512-byte blocks
    BYTE buffer[512];

    // Read the forensic image file
    while (fread(buffer, sizeof(BYTE), 512, file) == 512)
    {
        // Check for the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous JPEG file if open
            if (jpeg != NULL)
            {
                fclose(jpeg);
            }

            // Create a new JPEG file
            sprintf(filename, "%03i.jpg", counter);
            jpeg = fopen(filename, "w");
            if (jpeg == NULL)
            {
                fclose(file);
                printf("Could not create JPEG file.\n");
                return 1;
            }

            // Increase the counter for the next JPEG file
            counter++;
        }

        // Write the block to the JPEG file
        if (jpeg != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, jpeg);
        }
    }

    // Close the files
    fclose(file);
    if (jpeg != NULL)
    {
        fclose(jpeg);
    }

    return 0;
}
