graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 6
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 7
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 9
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 101
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 127
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 137
  ]
  edge [
    source 0
    target 3
    delay 29
    bw 77
  ]
  edge [
    source 1
    target 5
    delay 31
    bw 177
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 129
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 63
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 83
  ]
]
