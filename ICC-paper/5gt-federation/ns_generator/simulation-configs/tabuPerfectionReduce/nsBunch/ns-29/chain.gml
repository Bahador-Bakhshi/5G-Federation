graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 3
    memory 10
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 2
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 177
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 161
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 106
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 77
  ]
  edge [
    source 1
    target 5
    delay 32
    bw 176
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 168
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 198
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 55
  ]
]
