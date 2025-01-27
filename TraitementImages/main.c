#include "image_process.h"
#include <stdio.h>
#include <stdlib.h>
#include "file_operations.h"

int main(int argc, char *argv[]) {

    char path[1024];
    snprintf(path, sizeof(path), "%s", argv[1]);


    FILE* file = fopen(path, "rb");
    if (!file) {
        perror("❌ Erreur lors de l'ouverture du fichier pour l'écriture.");
        return -1;
    }

    FILE *file2 = fopen("result.txt", "w");
    if (!file2) {
        perror("❌ Erreur lors de l'ouverture du fichier pour l'écriture.");
        return -1;
    }

    FILE* file3 = fopen("test", "w");
	if (file3 == NULL) {
        perror("Error opening file");
    }

    const ImageData image_data = extract_image_text_data(path);

    Clusters clusters = find_clusters(image_data);


	if (clusters != NULL) {

    	for (int i = 0; i < image_data->height; i++) {
        	for (int j = 0; j < image_data->width; j++) {
            	fprintf(file3, "%d ", clusters->binary_mask[i][j]);
        	}
        	fprintf(file3, "\n");
    	}



    	update_binary_mask_with_largest_cluster(clusters);



        clusters = find_clusters_attributes(clusters);
    	display_clusters(clusters);


        int cluster_count = number_clusters(clusters);


    	Clusters current_cluster = clusters;

    	if (current_cluster != NULL) {
          	fprintf(file2, "%d\n", cluster_count);
    		while (current_cluster != NULL) {
        		fprintf(file2, "%s %d %d %d\n", color_to_string(current_cluster->color),
                		current_cluster->mid_x, current_cluster->mid_y, current_cluster->radius);
        		current_cluster = current_cluster->next;
       		}

    	}else {
      	fprintf(file2, "");
        }
        free_clusters(clusters);
   	}else {
      	fprintf(file2, "");
    }




	fclose(file);
    fclose(file2);
	fclose(file3);

    free_image_data(image_data);

    return 0;
}
