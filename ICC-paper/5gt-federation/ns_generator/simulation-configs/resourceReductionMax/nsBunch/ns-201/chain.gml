graph [
  node [
    id 0
    label 1
    disk 6
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 105
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 60
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 179
  ]
  edge [
    source 0
    target 3
    delay 33
    bw 130
  ]
  edge [
    source 1
    target 5
    delay 31
    bw 176
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 170
  ]
]
