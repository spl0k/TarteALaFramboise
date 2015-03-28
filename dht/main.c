#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "pi_dht_read.h"

int main(int argc, char** argv)
{
	int sensor = 0;
	int pin = 0;
	int retries = 1;
	int out_short = 0;
	int out_temp = 0;
	int out_humi = 0;

	// Parse command-line
	for(int i = 1; i < argc; ++i)
	{
		if(argv[i][0] == '-')
		{
			if(argv[i][1] == '-')
			{
				if(strcmp(argv[i], "--short") == 0) out_short = 1;
				else if(strcmp(argv[i], "--temperature") == 0) out_temp = 1;
				else if(strcmp(argv[i], "--humidity") == 0) out_humi = 1;
			}
			else
			{
				char* arg = argv[i];
				while(*(++arg))
				{
					switch(*arg)
					{
						case 's': out_short = 1; break;
						case 't': out_temp = 1; break;
						case 'h': out_humi = 1; break;
					}
				}
			}
		}
		else if(sensor == 0)
			sensor = atoi(argv[i]);
		else if(pin == 0)
			pin = atoi (argv[i]);
		else
			retries = atoi(argv[i]);
	}

	// Validate command-line args
	if(!out_temp && !out_humi)
	{
		out_temp = 1;
		out_humi = 1;
	}
	if(sensor == 0 || pin == 0)
	{
		fprintf(stderr, "Usage: %s <11|22|2302> <pin> [retries]\n", argv[0]);
		return 1;
	}

	if(sensor != DHT11 && sensor != DHT22 && sensor != AM2302)
	{
		fprintf(stderr, "Invalid sensor type. Possible values are:\n- 11 for DHT11\n- 22 for DHT22\n- 2302 for AM2302\n");
		return 2;
	}
	if(pin < 0 || pin > 31)
	{
		fprintf(stderr, "Invalid pin number.\n");
		return 2;
	}
	if(retries < 1)
		retries = 1;

	// Do the reading
	float temperature, humidity;
	int status;
	for(int i = 0; i < retries; ++i)
	{
		status = pi_dht_read(sensor, pin, &humidity, &temperature);
		if(status == DHT_SUCCESS)
			break;

		sleep_milliseconds(2000);
	}

	if(status != DHT_SUCCESS)
	{
		fprintf(stderr, "Error while trying to read data: %i\n", status);
		return status;
	}

	// Output the result
	char output[48] = { 0 };
	int pos = 0;
	if(out_temp)
		pos = sprintf(output, out_short ? "%.2f" : "Temperature: %.2f°C", temperature);
	if(out_humi)
		pos += sprintf(output + pos, out_short ? (pos ? " %.2f" : "%.2f") : (pos ? ", humidity: %.2f%%" : "Humidity: %.2f%%"), humidity);
	sprintf(output + pos, "\n");
	printf(output);

	return 0;
}

