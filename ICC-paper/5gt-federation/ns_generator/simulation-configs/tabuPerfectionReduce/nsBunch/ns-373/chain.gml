graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 16
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 7
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 4
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 119
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 178
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 71
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 115
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 177
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 145
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 137
  ]
]
