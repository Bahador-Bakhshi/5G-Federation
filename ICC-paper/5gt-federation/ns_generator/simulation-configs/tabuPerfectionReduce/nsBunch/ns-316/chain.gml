graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 13
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 6
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 2
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 14
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 83
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 150
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 190
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 149
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 66
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 173
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 182
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 172
  ]
]
