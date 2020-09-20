graph [
  node [
    id 0
    label 1
    disk 7
    cpu 2
    memory 6
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 7
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 2
    memory 11
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 116
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 188
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 62
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 195
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 86
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 68
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 132
  ]
]
