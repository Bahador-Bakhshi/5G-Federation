graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 2
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 8
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
    delay 33
    bw 91
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 154
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 109
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 178
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 126
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 56
  ]
]
