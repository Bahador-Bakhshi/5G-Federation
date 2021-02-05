graph [
  node [
    id 0
    label 1
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 16
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 197
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 111
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 153
  ]
  edge [
    source 0
    target 3
    delay 26
    bw 97
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 159
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 195
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 141
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 122
  ]
]
