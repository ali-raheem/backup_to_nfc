# Quick and Dirty data to Mifare 1K V0.1.3

Simply takes a file (<= 720 bytes) and writes it to a mifare 1k file using the ER301 interface.

Makes use of Marc de Verdelhan's 2013 code for YHY523U under MIT license.

My contributions also under MIT.

### Usage

Make sure you have the file to be written called datafile in the same directory as er301_backup

```
$ ./er301_backup
```

This will write datafile to the card and output a 'outfile' which is read from the card and automatically trimmed.

To verify run

```
$ diff -s datafile outfile
```

To recovery file

```
$ python er301_read.py
$ head -c LENGTH_IN_BYTES readfile > finalfile
```

Currently the readfile is not automatically trimmed, so make note of the written length and trim it with head.

finalfile should be identical to datafile.

### Changelog

* 2017/05/18 - Added readfile
  	       Removed some unused code in library.
* 2017/05/18 - Initial commit

### Todo

* Add meta data to first sector 32 bytes.
  * 2 bytes padding
  * 30 bytes unallocated? Description etc?