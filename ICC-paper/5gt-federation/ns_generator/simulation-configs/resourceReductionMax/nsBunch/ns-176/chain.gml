graph [
  node [
    id 0
    label 1
    disk 8
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 2
    memory 8
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 15
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 192
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 189
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 117
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 91
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 177
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 104
  ]
]
