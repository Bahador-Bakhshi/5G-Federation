graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 2
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 6
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 2
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 10
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 14
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 64
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 155
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 96
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 153
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 115
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 72
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 116
  ]
]
