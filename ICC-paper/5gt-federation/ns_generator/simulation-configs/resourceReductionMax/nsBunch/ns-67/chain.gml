graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 8
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 1
    memory 9
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 14
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 1
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 137
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 82
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 176
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 172
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 141
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 195
  ]
]
